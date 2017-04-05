import uuid

def get_img_name():
    '''产生唯一的图片名称，避免文件重复'''
    return str(uuid.uuid4())

def handle_uploaded_file(f):
    name = get_img_name() + '.'+f.name.split('.')[-1]
    name = '/'.join(['user_app','static','img',name])
    print(name)
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
