import numpy as np 

def function(x):

	k9 = x
	r8 = x
	paths = []
	try:
		if r8 < 3:
			k9 = r8/k9
			paths.append(1)
		else:
			k9 = k9/3
			k9 = k9-x
			k9 = r8*k9
			paths.append(2)
		if x <= 5:
			x = x-4
			k9 = x*2
			k9 = 9+k9
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		r8 = k9**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))