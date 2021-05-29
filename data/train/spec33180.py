import numpy as np 

def function(x):

	b4 = x
	r3 = x
	paths = []
	try:
		if r3 < 6:
			r3 = r3*2
			paths.append(1)
		else:
			r3 = 9*0
			x = x-b4
			paths.append(2)
		if r3 > 1:
			r3 = b4*8
			x = 1/9
			paths.append(3)
		else:
			b4 = 2-1
			r3 = r3-5
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		b4 = r3**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))