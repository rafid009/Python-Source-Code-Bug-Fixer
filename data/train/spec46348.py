import numpy as np 

def function(x):

	l6 = x
	o0 = x
	paths = []
	try:
		if x < 0:
			l6 = l6+9
			l6 = l6-4
			o0 = o0+3
			paths.append(1)
		else:
			o0 = o0*0
			o0 = 0+x
			x = 4/x
			paths.append(2)
		if l6 <= 9:
			l6 = l6-3
			l6 = o0+l6
			o0 = 7+l6
			paths.append(3)
		else:
			o0 = o0*1
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		l6 = o0**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))