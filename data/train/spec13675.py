import numpy as np 

def function(x):

	j5 = 4
	v3 = 1
	paths = []
	try:
		if v3 >= 3:
			v3 = 1/v3
			x = x*3
			x = 7*2
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if v3 > 8:
			v3 = v3+6
			x = 6+x
			paths.append(3)
		else:
			v3 = j5+v3
			j5 = x-1
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		v3 = j5**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))