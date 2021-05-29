import numpy as np 

def function(x):

	v7 = x
	j2 = 4
	x = 1
	paths = []
	try:
		if j2 >= 4:
			x = v7+7
			x = x*j2
			paths.append(1)
		else:
			j2 = j2+j2
			x = x/4
			paths.append(2)
		if x > 6:
			j2 = 3*j2
			paths.append(3)
		else:
			j2 = x+j2
			x = 7+1
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