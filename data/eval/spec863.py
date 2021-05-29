import numpy as np 

def function(x):

	w3 = x
	o3 = x
	paths = []
	try:
		if w3 > 0:
			x = x+9
			o3 = o3+w3
			x = x/o3
			paths.append(1)
		else:
			x = w3/1
			paths.append(2)
		if o3 <= 5:
			x = o3-o3
			o3 = 2-6
			o3 = 8*8
			paths.append(3)
		else:
			o3 = o3*0
			w3 = 5+w3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		o3 = w3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))