from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="converted.json",
    path_in_repo="converted.json",
    repo_id="sbchild/for-you",
    repo_type="dataset",
)
