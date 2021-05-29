import numpy as np 

def function(x):

	r3 = 8
	s9 = x
	x = x
	paths = []
	try:
		if x > 7:
			r3 = 2+r3
			paths.append(1)
		else:
			r3 = r3*1
			x = x*2
			paths.append(2)
		if r3 > 8:
			x = x+0
			r3 = r3-2
			r3 = 0*9
			paths.append(3)
		else:
			r3 = 7+r3
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))