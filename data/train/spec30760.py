import numpy as np 

def function(x):

	k8 = 4
	q5 = 7
	x = 0
	paths = []
	try:
		if k8 <= 1:
			x = x*6
			k8 = 4*5
			paths.append(1)
		else:
			x = 6-x
			x = 6*1
			x = k8+0
			paths.append(2)
		if q5 >= 4:
			q5 = q5+x
			x = 2-x
			q5 = q5+k8
			paths.append(3)
		else:
			q5 = q5+x
			x = q5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))