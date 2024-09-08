import requests
import sys

def download_url(link, file_name, show_progress=True):
    with open(file_name, "wb") as f:
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                if show_progress:
                    done = int(50 * dl / total_length)
                    done_str = "="*done
                    remain_str = " "*(50-done)
                    percent    = dl / total_length * 100
                    sys.stdout.write(f"\r[{done_str}{remain_str}] {percent:.0f}%")    
                    sys.stdout.flush()