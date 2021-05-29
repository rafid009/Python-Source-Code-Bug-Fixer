import numpy as np 

def function(x):

	k9 = x
	u3 = x
	paths = []
	try:
		if x > 0:
			x = x-7
			k9 = 4*k9
			paths.append(1)
		else:
			u3 = u3/4
			k9 = k9+7
			paths.append(2)
		if k9 < 4:
			x = x*2
			paths.append(3)
		else:
			k9 = 2-6
			x = k9/x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))