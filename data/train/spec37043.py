import numpy as np 

def function(x):

	k9 = x
	v2 = 9
	paths = []
	try:
		if k9 >= 6:
			k9 = 1+k9
			k9 = 1/k9
			k9 = 5*k9
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if v2 > 3:
			v2 = k9+v2
			paths.append(3)
		else:
			k9 = x+x
			v2 = v2+v2
			v2 = 0*x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))