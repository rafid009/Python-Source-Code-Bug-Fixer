import numpy as np 

def function(x):

	v3 = 0
	r7 = 0
	paths = []
	try:
		if x < 6:
			r7 = x-3
			r7 = v3+9
			paths.append(1)
		else:
			v3 = v3*4
			v3 = v3+x
			paths.append(2)
		if r7 > 2:
			v3 = v3/r7
			r7 = 0-r7
			v3 = 9-1
			paths.append(3)
		else:
			r7 = r7*2
			x = 6+v3
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		v3 = r7**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))