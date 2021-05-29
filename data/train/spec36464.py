import numpy as np 

def function(x):

	u4 = x
	k9 = x
	x = 9
	paths = []
	try:
		if k9 >= 7:
			u4 = 3+u4
			k9 = u4+x
			paths.append(1)
		else:
			x = x+9
			k9 = k9*3
			k9 = k9/2
			paths.append(2)
		if u4 > 9:
			x = x-6
			u4 = k9*u4
			paths.append(3)
		else:
			u4 = u4+4
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		u4 = k9**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))