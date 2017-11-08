import numpy as np
class Perception(object):
	def __int__(self,eta=0.01,n_iter=10):
		self.eta=eta
		self.n_iter=n_iter
		pass
	def fit(self,x,y):
		self.w_=np.zeros(1+x.shape[1]);
		self.error=[]
		pass