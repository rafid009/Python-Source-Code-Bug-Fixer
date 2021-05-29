import numpy as np 

def function(x):

	v5 = x
	j6 = 9
	paths = []
	try:
		if x < 7:
			j6 = 0+j6
			v5 = 9/v5
			x = j6-x
			paths.append(1)
		else:
			x = j6-4
			v5 = 0*v5
			v5 = v5/9
			paths.append(2)
		if j6 > 1:
			j6 = v5*j6
			x = x*4
			paths.append(3)
		else:
			v5 = v5-6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		v5 = j6**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))