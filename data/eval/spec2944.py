import numpy as np 

def function(x):

	t5 = x
	k0 = 7
	paths = []
	try:
		if k0 <= 7:
			x = t5+x
			x = x-4
			x = x*8
			paths.append(1)
		else:
			x = k0+2
			x = x*k0
			t5 = 7/6
			paths.append(2)
		if t5 >= 9:
			x = x/6
			x = t5+x
			paths.append(3)
		else:
			t5 = 7*t5
			k0 = 6-t5
			t5 = t5*t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))