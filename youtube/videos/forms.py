from django import forms

class VideoUploadForm(forms.Form):
    title=forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Enter Video Title"})
    )

    description=forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class":"form-input",
            "placeholder":"Enter Video Description"
        })
    )

    video_file=forms.FileField(
        widget=forms.FileInput(attrs={
            "class":"form-input",
            "accept":"video/*",
        })
    )

    def clean_video_file(self):
        video=self.cleaned_data.get("video_file")
        if video:
            if video.size > 100 * 1024 * 1024:
                raise forms.ValidationError("Video file must be less than 100MB")
            allowed_types=["video/mp4","video/avi","video/mov","video/wmv","video/flv","video/mpeg","video/mpg","video/m4v","video/webm","video/ogg","video/mkv"]
            if video.content_type not in allowed_types:
                raise forms.ValidationError("Invalid video file type")

        return video
