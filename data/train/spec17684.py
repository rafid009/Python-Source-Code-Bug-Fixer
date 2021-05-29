import numpy as np 

def function(x):

	k8 = x
	f1 = 2
	paths = []
	try:
		if f1 < 7:
			k8 = k8*9
			paths.append(1)
		else:
			f1 = f1*x
			f1 = 0*2
			f1 = 7*6
			paths.append(2)
		if f1 < 4:
			f1 = k8+8
			x = 6+5
			x = x+f1
			paths.append(3)
		else:
			x = 0*3
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		f1 = k8**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))