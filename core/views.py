from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View
from django.contrib.auth import get_user_model
from core.models import Follower,Post,Like,Comment,SavedPost
from core.forms import PostCreateForm
from django.db.models import Count
User=get_user_model()

#SECTION - <<<<<<<<<<<<<<<Dashboard >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
# Create your views here.
class dashboard(View):
    
    template_name='core/dashboard.html'
    
    def get(self, request, *arga, **kwargs):
        all_post=Post.objects.all()
        
        context={'all_posts':all_post}
        
        return render(request, self.template_name, context=context)
        
        
    
#SECTION -<<<<<<<<<<<<<<<<<<<<<<Post create and upload >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

 
class UploadPost(TemplateView):
    template_name='core/UploadPost.html'
    
    form_class = PostCreateForm

    def get(self, request, *arga, **kwargs):
        form = self.form_class()
        all_posts = Post.objects.all()
        context = { 'form': form, 'all_posts': all_posts }
        return render(request, self.template_name, context=context)
    
#SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<<Post Delete view>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class post_delete_view(View):
    
    def post (self,request,*args , **kwargs):
        
        post_id=kwargs.get('id')
        
        try:
        
            post_obj= Post.objects.get(pk=post_id)
            
        except Exception as e:
            return redirect(request.META.get('HTTP_REFERER'))
        
        if request.user == post_obj.user:
            
            post_obj.delete()
        
        return redirect(request.META.get('HTTP_REFERER'))
            
        
        

class PostCreateView(View):
    
    form_class = PostCreateForm
    
    def post (self,request,*args , **kwargs):
        
        form_p=self.form_class(request.POST,request.FILES)
        
        if form_p.is_valid():
            
            form_p.save()
            
            return redirect('dashboard')
        else:
            context={'form':form_p}
            return redirect('UploadPost',context=context)
        
#SECTION - <<<<<<<<<<<<<<<<<<<<<<< Post Details View >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class PostDetailsView(View):
    
    template_name='core/post_details.html'
    
    def get(self, request, *arga, **kwargs):
        
        post_id=kwargs.get('id')
        
        try:
        
            post_obj=Post.objects.get(pk=post_id)
            
        except Exception as e :
            return redirect(request.META.get('HTTP_REFERER'))
        
        #NOTE -<<<<<<<<<<<<<<<<<<<<<<  Check the like and unlike >>>>>>>>>>>>>
        # breakpoint()
        try:
                Like.objects.get(user=request.user, Post=post_id)
                liked_this_post = True
        except Exception as e:
                liked_this_post = False
                
        #NOTE -  <<<<<<<<<<<<<<<Check  the shave post or not >>>>>>>>>>>>>>>>>.>>>>>>>>>
        try:
                SavedPost.objects.get(user=request.user, post=post_id)
                post_this_post = True
        except Exception as e:
                post_this_post = False
                
        
                 
        context={'post': post_obj,'liked_this_post': liked_this_post,'post_saved':post_this_post}
        
        return render(request, self.template_name,context=context)
    
    
    
#SECTION -  <<<<<<<<<<<<<<<<<Post Like and Dislike View >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class PostLikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        try:
            Like.objects.get(user=request.user, pk=post_id)
        except Exception as e:
            post = get_object_or_404(Post, pk=post_id)
            Like.objects.create(user=request.user, Post=post)

        return redirect(request.META.get('HTTP_REFERER'))
    
class PostUnlikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        if request.user.is_authenticated:
            try:
                # like_obj = Like.objects.get(user=request.user, post_id=post_id)
                # post = get_object_or_404(Post, pk=post_id)
                like_obj=Like.objects.get(user=request.user, Post=post_id)

                like_obj.delete()
            except Like.DoesNotExist:
                pass

        return redirect(request.META.get('HTTP_REFERER'))
    
    
#SECTION -<<<<<<<<<<<<<<<<<<<<<<  POst Comment view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class PostCommentView(View):
    def post(self, request, *args, **kwargs):
        
        post_id = kwargs.get('id')
        
        comment_text = request.POST.get('comment_text')

        
        post = get_object_or_404(Post, pk=post_id)      
        user = request.user  # Assuming you have user authentication

        # Correct way to create a Comment object
        comment = Comment(Post=post, user=user, text_comment=comment_text)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    

    
    
#SECTION -  <<<<<<<<<<<<<<<Post save view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class PostsaveView(View):
    
    def post (self,request,*args , **kwargs):
        post_id = kwargs.get('id')
        
        try:
            post_obj = Post.objects.get(pk=post_id)
        except Exception as e:
            
            return redirect(request.META.get('HTTP_REFERER'))

            

        try:
            SavedPost.objects.create(post_id=post_id)
        except Exception as e:
            return redirect(request.META.get('HTTP_REFERER'))


        return redirect(request.META.get('HTTP_REFERER'))
    
class PostUnsaveView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        
        try:
            savedpost_obj = SavedPost.objects.get(post_id=post_id)
            savedpost_obj.delete()
        except Exception as e:
            pass       

        return redirect(request.META.get('HTTP_REFERER'))
    
    
#SECTION -  <<<<<<<<<<<<<<<<<<<nab var post save view >>>>>>>>>>>>>>>>>>>>


class SavedPostsView(View):
    template_name = 'core/saved_posts.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    
#SECTION - >>><<<<<<<<<<<<< Liked View >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class LikedPostsView(View):
    template_name = 'core/liked_posts.html'
    def get(self, request, *args, **kwargs):
        # breakpoint()
        return render(request, self.template_name)
    
    
    
#SECTION -><<<<<<<<<<<<<<<<<<<<<<<<  Explore view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class ExplorePostsView(View):
    template_name = 'core/posts_explore.html'
    def get(self, request, *args, **kwargs):

        all_posts = Post.objects.annotate(count=Count('like')).order_by('-count')
        context = {'all_posts': all_posts}
        return render(request, self.template_name, context=context)


#SECTION -  ,<<,,,,,,,,,,<<<<<<Follower and UnFollowing >>>>>>.,,,,,,,,,,,,,,,,,,,,,,,,,,>>>


class FollowDoneView(View):
        
    def post (self,request,*args , **kwargs):
        
        followed_user_id=request.POST.get('followed_user_id')
        
        followed_user_obj=User.objects.get(pk=followed_user_id)
        
        try:
            Follower.objects.get(user=request.user, followed=followed_user_obj)
        except Exception as e:
            follow_obj = Follower.objects.create(followed=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER'))
    
    
class UnFollowDoneView(View):
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)

        try:
            follow_obj = Follower.objects.get(user=request.user, followed=unfollowed_user_obj)
            follow_obj.delete()
        except Exception as e:
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))
        
        
    

