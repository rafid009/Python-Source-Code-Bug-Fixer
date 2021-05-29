import numpy as np 

def function(x):

	v3 = 7
	j2 = 3
	paths = []
	try:
		if j2 >= 0:
			j2 = j2+x
			paths.append(1)
		else:
			j2 = j2-2
			v3 = j2*v3
			paths.append(2)
		if x <= 0:
			x = x-2
			x = x*j2
			v3 = x-4
			paths.append(3)
		else:
			j2 = 3-j2
			x = x-2
			v3 = v3+4
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))