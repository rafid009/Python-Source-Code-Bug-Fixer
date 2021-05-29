import numpy as np 

def function(x):

	o3 = 9
	m6 = x
	paths = []
	try:
		if o3 > 7:
			x = x*m6
			o3 = o3*0
			x = 2+x
			paths.append(1)
		else:
			o3 = o3*m6
			m6 = o3/m6
			m6 = 3/4
			paths.append(2)
		if m6 >= 0:
			o3 = o3-4
			x = x*o3
			paths.append(3)
		else:
			m6 = x-9
			m6 = 5/m6
			m6 = 4+m6
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))