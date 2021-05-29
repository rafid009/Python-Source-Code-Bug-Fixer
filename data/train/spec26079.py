import numpy as np 

def function(x):

	r6 = 8
	k9 = 4
	paths = []
	try:
		if r6 >= 4:
			k9 = 5+k9
			r6 = r6*x
			paths.append(1)
		else:
			k9 = k9/r6
			paths.append(2)
		if x > 8:
			r6 = 9+2
			x = 1-3
			x = 0/2
			paths.append(3)
		else:
			k9 = k9/5
			k9 = 0/3
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		k9 = r6**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))