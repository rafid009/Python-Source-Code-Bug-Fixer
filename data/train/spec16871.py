import numpy as np 

def function(x):

	l5 = x
	v8 = 0
	paths = []
	try:
		if x < 2:
			v8 = v8*8
			x = x/2
			v8 = v8/5
			paths.append(1)
		else:
			x = 3*4
			x = x-4
			paths.append(2)
		if l5 <= 4:
			v8 = 5+v8
			l5 = 2*l5
			v8 = 1-v8
			paths.append(3)
		else:
			x = x+5
			l5 = x-5
			x = 1*2
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		v8 = l5**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))