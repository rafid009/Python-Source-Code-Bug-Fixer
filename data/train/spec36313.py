import numpy as np 

def function(x):

	v0 = x
	w7 = 0
	paths = []
	try:
		if v0 <= 5:
			x = v0-1
			paths.append(1)
		else:
			v0 = v0+4
			w7 = 5+w7
			v0 = v0+9
			paths.append(2)
		if w7 < 4:
			v0 = w7*v0
			w7 = 2+w7
			v0 = v0*1
			paths.append(3)
		else:
			x = 0*w7
			x = x*0
			v0 = v0+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))