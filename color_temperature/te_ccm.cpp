#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cmath>
#include <algorithm>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;
using namespace std;

Mat te_to_ccm(float myte);

int main()
{
    float myte = 8120;
    Mat my_matrix = te_to_ccm(myte);
    
    cout<<my_matrix<<endl;
    return 0;
}

Mat te_to_ccm(float myte)
{
    float te[9] = {1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000};
    vector<Mat> te_matrix(9);

    Mat te_matrix1 = (Mat_<float>(3, 3) << 1, 1, 1, 1, 1, 1, 1, 1, 1);
    Mat te_matrix2 = (Mat_<float>(3, 3) << 2, 2, 2, 2, 2, 2, 2, 2, 2);
    Mat te_matrix3 = (Mat_<float>(3, 3) << 3, 3, 3, 3, 3, 3, 3, 3, 3);
    Mat te_matrix4 = (Mat_<float>(3, 3) << 4, 4, 4, 4, 4, 4, 4, 4, 4);
    Mat te_matrix5 = (Mat_<float>(3, 3) << 5, 5, 5, 5, 5, 5, 5, 5, 5);
    Mat te_matrix6 = (Mat_<float>(3, 3) << 6, 6, 6, 6, 6, 6, 6, 6, 6);
    Mat te_matrix7 = (Mat_<float>(3, 3) << 7, 7, 7, 7, 7, 7, 7, 7, 7);
    Mat te_matrix8 = (Mat_<float>(3, 3) << 8, 8, 8, 8, 8, 8, 8, 8, 8);
    Mat te_matrix9 = (Mat_<float>(3, 3) << 9, 9, 9, 9, 9, 9, 9, 9, 9);

    te_matrix[0] = te_matrix1; te_matrix[1] = te_matrix2; te_matrix[2] = te_matrix3;
    te_matrix[3] = te_matrix4; te_matrix[4] = te_matrix4; te_matrix[5] = te_matrix6;
    te_matrix[6] = te_matrix7; te_matrix[7] = te_matrix8; te_matrix[8] = te_matrix9;
    
    Mat my_matrix;
    if(myte < te[0]){
        my_matrix = te_matrix[0];
    }
    else if(myte > te[8]){
        my_matrix = te_matrix[8];
    }
    else{
        for(int i=0; i<sizeof(te); i++){
            if(te[i] > myte){
                float g = (myte - te[i-1])/(te[i] - te[i-1]);
                my_matrix = g*te_matrix[i] + (1-g)*te_matrix[i-1];          
                break;                
            }
        }
    }
    return my_matrix;
}



