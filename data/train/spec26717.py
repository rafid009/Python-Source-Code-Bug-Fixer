import numpy as np 

def function(x):

	v8 = 0
	w6 = x
	paths = []
	try:
		if x <= 2:
			v8 = x+0
			x = 4/x
			paths.append(1)
		else:
			x = 3+x
			w6 = w6-3
			paths.append(2)
		if w6 <= 4:
			x = x*w6
			v8 = v8/x
			v8 = v8+9
			paths.append(3)
		else:
			w6 = w6*1
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		w6 = v8**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))