import numpy as np 

def function(x):

	v3 = x
	j8 = 1
	paths = []
	try:
		if v3 < 0:
			v3 = 4+v3
			j8 = 7/5
			v3 = v3+1
			paths.append(1)
		else:
			j8 = j8/2
			paths.append(2)
		if x < 0:
			j8 = 0*j8
			v3 = v3+0
			paths.append(3)
		else:
			x = 9+x
			j8 = j8+9
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		j8 = v3**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))