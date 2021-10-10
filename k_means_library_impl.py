import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
import RGB_to_gray
class K_means:
    def standardize(X):
        h,w,c = np.shape(X)
        X = X/255
        X = X.reshape(w*h,c)
        return X,h,w

    def image_processing(img_path):
        img = Image.open(img_path)
        arr = np.asarray(img)
        img.close()
        return arr

    def k_means_clustering(n_clusters,X):
        k_means = KMeans(n_clusters).fit(X)
        compressed_img_array = k_means.predict(X)
        return compressed_img_array,k_means.cluster_centers_

    def show_img(index,centroid,img):
        centroid = np.array(centroid)
        recovered_image = centroid[index.astype(int),:]
        recovered = np.reshape(recovered_image, (img.shape[0], img.shape[1],
                                                        img.shape[2]))
    
        plt.imshow(recovered)
        plt.show()

def calculate_compressed_image(file_name,n_clusters = 64):
    obj = K_means
    img_array = obj.image_processing(file_name)
    standardized_array,h,w = obj.standardize(img_array)
    compressed_img_array,centroids = obj.k_means_clustering(n_clusters,standardized_array)
    obj.show_img(compressed_img_array,centroids,img_array)



