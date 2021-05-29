import numpy as np 

def function(x):

	k0 = 1
	f0 = 0
	paths = []
	try:
		if f0 <= 8:
			f0 = f0+7
			f0 = 2+x
			paths.append(1)
		else:
			f0 = 6+f0
			paths.append(2)
		if k0 < 0:
			k0 = k0*0
			f0 = f0+4
			paths.append(3)
		else:
			k0 = f0+k0
			f0 = 4*4
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		f0 = k0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))