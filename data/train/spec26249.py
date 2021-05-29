import numpy as np 

def function(x):

	r6 = x
	k9 = x
	paths = []
	try:
		if x >= 6:
			r6 = x+5
			k9 = k9-2
			x = 2*x
			paths.append(1)
		else:
			r6 = x*0
			paths.append(2)
		if r6 < 8:
			k9 = 4*k9
			x = 0*x
			paths.append(3)
		else:
			r6 = 8-r6
			k9 = 0+x
			x = 3*9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))