import numpy as np 

def function(x):

	v8 = 3
	k8 = x
	paths = []
	try:
		if k8 <= 5:
			v8 = x*0
			v8 = v8+x
			k8 = x+v8
			paths.append(1)
		else:
			v8 = v8/9
			x = k8/2
			v8 = 7-k8
			paths.append(2)
		if v8 <= 6:
			x = x-x
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		k8 = v8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))