from bing_image_downloader import downloader
downloader.download("famous footballer", limit=50,  output_dir='famous footballer', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)