import numpy as np 

def function(x):

	v1 = x
	a6 = x
	paths = []
	try:
		if x < 7:
			v1 = v1/x
			v1 = v1-8
			a6 = 5+1
			paths.append(1)
		else:
			x = x*9
			v1 = x/4
			a6 = 2+a6
			paths.append(2)
		if x < 2:
			a6 = 7+a6
			x = x/9
			a6 = 7+a6
			paths.append(3)
		else:
			x = x+a6
			v1 = x+x
			x = a6-7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))