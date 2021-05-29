import numpy as np 

def function(x):

	v1 = 1
	j6 = 2
	paths = []
	try:
		if v1 < 1:
			j6 = 4*j6
			v1 = x-j6
			x = 2/9
			paths.append(1)
		else:
			j6 = j6-6
			paths.append(2)
		if x <= 7:
			j6 = j6-j6
			v1 = 5*1
			v1 = j6*0
			paths.append(3)
		else:
			x = 9+x
			v1 = 7+v1
			j6 = j6+0
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		v1 = j6**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))