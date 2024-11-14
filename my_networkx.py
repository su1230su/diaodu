import cv2

def get_video_info(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("无法打开视频文件")
        return

    # 获取视频总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 获取视频时长（秒）
    duration = total_frames / fps

    print(f"视频总帧数: {total_frames}")
    print(f"视频帧率: {fps}")
    print(f"视频时长（秒）: {duration}")

    cap.release()

if __name__ == "__main__":
    video_path = "D:\桌面\数据\2.2024年中国研究生数学建模竞赛E题数据\2024年中国研究生数学建模竞赛E题数据\2024年中国研究生数学建模竞赛E题数据"
    get_video_info(video_path)


