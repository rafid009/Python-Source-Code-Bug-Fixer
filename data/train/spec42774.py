import numpy as np 

def function(x):

	f0 = x
	p9 = x
	paths = []
	try:
		if p9 > 4:
			f0 = f0*f0
			x = 1+x
			p9 = p9*8
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x > 0:
			f0 = p9*f0
			paths.append(3)
		else:
			x = x/7
			f0 = 3+f0
			f0 = f0/7
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		f0 = p9**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))