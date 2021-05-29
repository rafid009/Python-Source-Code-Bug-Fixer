import numpy as np 

def function(x):

	v3 = 4
	k9 = x
	paths = []
	try:
		if k9 < 4:
			k9 = 0+8
			v3 = 0*3
			x = 0-2
			paths.append(1)
		else:
			v3 = v3*0
			x = x+v3
			v3 = v3-1
			paths.append(2)
		if k9 < 8:
			x = 2/x
			x = 7*x
			paths.append(3)
		else:
			v3 = 0*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))