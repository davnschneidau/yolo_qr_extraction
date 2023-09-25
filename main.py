from yolo import YOLOv5
import cv2

def main():

    cap = cv2.VideoCapture(0)
    yolo = YOLOv5()
    while True:
        ret, frame = cap.read()

        if ret:
            objects, out = yolo.detect(frame)
            if len(objects) > 0:
                for x1, y1, x2, y2  in objects:

                    cropped = out[y1:y2, x1:x2]

                    
            cv2.imshow("frame", out)
            
        if cv2.waitKey(5) & 0xFF == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()