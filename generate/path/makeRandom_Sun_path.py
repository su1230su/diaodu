import random
import string

def float_random(count, average, begin, end):
    # print "wzh_random"
    numarr = [0 for x in range(2)];
    i = 0;
    while (1):

        num = random.uniform(begin, end);
        # 取两位小数
        num_first = round(num, 2);

        # 第二个数
        num_second = average * 2 - num_first;

        if (num_second >= begin and num_second <= end):
            numarr[i] = num_first;
            i = i + 1;
            numarr[i] = num_second;
            break

    return numarr;

def random_float(count,average,begin,end):

    numarr_count = 0;
    numarr = [0 for x in range(count)];
    if(count % 2):
        count-=1
        count = int(count / 2)

        for i in range(count):
            list = float_random(count, average, begin, end)
            j = 0;
            for j in range(len(list)):
                numarr[numarr_count] = list[j];
                numarr_count += 1;
        numarr[count-1]=average
    else:
        count=int(count/2)

        for i in range (count):
            list = float_random (count, average, begin, end)
            j = 0;
            for j in range (len(list)):
                 numarr[numarr_count] = list[j];
                 numarr_count += 1;
    content = '';
    #打乱排序
    random.shuffle(numarr);
 #   print ("数据打乱：");
  #  print (numarr)
    a=1
    return numarr


#调用测试产生实型随机数
#a=random_float(400,5.5,0,10);
#print (a)