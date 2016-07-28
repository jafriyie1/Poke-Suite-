from OpenFiles import OpenImageFiles 
from numpy import array
from sklearn import svm 
from sklearn import grid_search
from sklearn import cross_validation
from sklearn import metrics
import time
import numpy as np
import random
import pickle

def implementation():
	"""Implementation function for SVM Classifier"""

	#path = input("Please enter absolute path: ")
	temp_path = "/Users/Joel/Desktop/Joel's Poke Suite/Phase 2/Poke Pictures Train"
	obj = OpenImageFiles(temp_path)
	data = obj.getOpenFiles()
	#test_picture = data[rand_int]
	#np_training_outputs = array([[1] for x in range(728)]).T


	temp_path_non = "/Users/Joel/Desktop/Joel's Poke Suite/Phase 2/Not Poke Pictures"
	obj = OpenImageFiles(temp_path_non)
	data_not = obj.getOpenFiles()
	#test_p = data_not[two_int]
	#np_training_outputs_non = array([[0] for x in range(56)]).T

	full_data  = array(data + data_not)
	nsamples, nx, ny = full_data.shape
	final_dataset = full_data.reshape((nsamples, nx*ny))
	target = array(([1] * len(data)) + ([0]* len(data_not))).T
	x_train, x_test, y_train, y_test = cross_validation.train_test_split(final_dataset,
            target, test_size=0.20)

	paramters = {"kernel":['linear', 'rbf', 'poly'], "C": [0.1,1,10,100,1000],
				"gamma": [.01,.001,.00001]}

	print(full_data)
	print("Training....")
	start = time.time()
	clf = grid_search.GridSearchCV(svm.SVC(), paramters).fit(x_train, y_train)
	classifier_results = str(clf.best_estimator_)
	print(classifier_results)
	prediction = clf.predict(x_test)
	score = str(metrics.accuracy_score(y_test, prediction))

	print("Finished training.")
	end = time.time()
	duration = str(end - start)
	current_pickled = clf
	log = open("details.txt", "w")
	log.write("The amount of time it took the model to train was: %s seconds \n" % duration)
	log.write(classifier_results)
	log.write('\n')
	log.write("The accuracy for the model is: %s \n" % score)
	log.close()
	f = open("poke_svm_trained.pkl", "wb+")
	pickle.dump(current_pickled, f)
	f.close()


if __name__ == "__main__":
	implementation()