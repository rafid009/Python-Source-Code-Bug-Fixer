import numpy as np 

def function(x):

	v7 = x
	u3 = 3
	paths = []
	try:
		if x <= 4:
			x = x-2
			v7 = 3+v7
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x < 2:
			v7 = v7+1
			x = 6*0
			paths.append(3)
		else:
			u3 = 6*7
			x = 6/u3
			x = v7/9
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))