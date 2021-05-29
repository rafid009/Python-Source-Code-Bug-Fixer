import numpy as np 

def function(x):

	v3 = 5
	o5 = 4
	paths = []
	try:
		if x > 3:
			x = 8*x
			x = x*9
			paths.append(1)
		else:
			o5 = o5*x
			paths.append(2)
		if o5 <= 7:
			v3 = v3+2
			o5 = x/2
			v3 = o5+1
			paths.append(3)
		else:
			v3 = x+v3
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