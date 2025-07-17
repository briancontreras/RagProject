import zipfile
import base64
import io


def read_zip(file):

    if isinstance(file,str):
        if file.endswith('.zip') or '/' in file or '\\' in file:
            return zipfile.ZipFile(file,mode='r')
        else:
            try:
                zip_bytes = base64.b64decode(file)
                zip_buffer = io.BytesIO(zip_bytes)
                return zipfile.ZipFile(zip_buffer, mode='r')
            except Exception as e:
                raise ValueError(f"Gang this isn't base 64 encoded twin : {e}")
    else:
        return zipfile.ZipFile(file,mode='r')
def process_zip(zipfile):
    file_info = []

    for file_info in zipfile.filelist:
        file_info.append({
            'filename' : file_info.filename,
            'file_size' : file_info.size,
            'compress_size' : file_info.compress_size,
            'date_time' : file_info.date_time
        })
    return {
        'files' : file_info,
        'total_files' : len(file_info),
        'zip_object' : zipfile
    }
def extract_all_from_base64_zip(base64_zip, extract_path=None):
    """Extract all files from base64 ZIP"""
    try:
        zip_bytes = base64.b64decode(base64_zip)
        zip_buffer = io.BytesIO(zip_bytes)
        
        with zipfile.ZipFile(zip_buffer, mode='r') as zip_file:
            if extract_path:
                zip_file.extractall(extract_path)
            else:
                # Return dictionary with filename: content
                extracted_files = {}
                for filename in zip_file.namelist():
                    extracted_files[filename] = zip_file.read(filename)
                return extracted_files
    except Exception as e:
        raise ValueError(f"Error extracting base64 ZIP: {e}")