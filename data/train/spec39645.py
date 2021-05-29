import numpy as np 

def function(x):

	v1 = 7
	q5 = x
	paths = []
	try:
		if x < 3:
			v1 = v1*6
			v1 = q5+q5
			x = 1+x
			paths.append(1)
		else:
			v1 = v1-x
			paths.append(2)
		if v1 < 8:
			v1 = v1+v1
			paths.append(3)
		else:
			x = 6/3
			q5 = 5+x
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