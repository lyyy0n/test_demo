import oss2

# 生成示例AK和SK
access_key_id = 'LTAS1CG5DUW703CCE9J3'
secret_access_key = 'Z4VXIrJMdmBO3D68D1bzZbI/IGsutW9noKfKoyr0'

# 设置你的阿里云账号相关信息
bucket_name = 'my-bucket'  # 你的Bucket名称
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'  # 根据实际情况选择合适的Endpoint
local_file_path = './example.txt'  # 本地文件路径
object_name = 'example.txt'  # 在OSS中的目标文件名

# 创建Bucket实例
auth = oss2.Auth(access_key_id, secret_access_key)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# 上传文件
def upload_file():
    try:
        result = bucket.put_object_from_file(object_name, local_file_path)
        print("Upload success. HTTP response status:", result.status)
    except oss2.exceptions.OssError as e:
        print("Failed to upload file. Error:", str(e))

if __name__ == '__main__':
    print(f"Using Access Key ID: {access_key_id}")
    print(f"Using Secret Access Key: {secret_access_key}")
    upload_file()
