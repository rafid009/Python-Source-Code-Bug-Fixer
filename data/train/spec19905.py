import numpy as np 

def function(x):

	v8 = 3
	n1 = 5
	x = x
	paths = []
	try:
		if n1 < 1:
			x = 8*x
			n1 = n1+5
			n1 = n1+5
			paths.append(1)
		else:
			n1 = n1/x
			v8 = n1*v8
			v8 = v8/9
			paths.append(2)
		if v8 <= 0:
			v8 = 6*0
			x = x-8
			paths.append(3)
		else:
			n1 = n1/5
			x = x/x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		v8 = n1**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))