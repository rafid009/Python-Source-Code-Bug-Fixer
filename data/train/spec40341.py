import numpy as np 

def function(x):

	k1 = 9
	j2 = x
	paths = []
	try:
		if k1 <= 3:
			x = 9+x
			x = x*k1
			j2 = 3-j2
			paths.append(1)
		else:
			x = 0-x
			k1 = 2-9
			k1 = k1/3
			paths.append(2)
		if x > 6:
			x = x*j2
			k1 = j2-1
			j2 = x*2
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		k1 = j2**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))