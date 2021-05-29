import numpy as np 

def function(x):

	q6 = x
	v3 = x
	paths = []
	try:
		if v3 < 1:
			v3 = v3/4
			q6 = 5*q6
			paths.append(1)
		else:
			v3 = v3*3
			paths.append(2)
		if x >= 1:
			v3 = 7*v3
			q6 = x+q6
			paths.append(3)
		else:
			x = x*0
			v3 = v3*2
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		v3 = q6**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))