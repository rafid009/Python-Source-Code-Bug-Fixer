import numpy as np 

def function(x):

	o0 = 5
	m3 = 4
	paths = []
	try:
		if m3 < 9:
			m3 = 2*m3
			paths.append(1)
		else:
			x = 6*0
			x = x/o0
			m3 = x*m3
			paths.append(2)
		if x > 4:
			o0 = x/m3
			o0 = o0-9
			paths.append(3)
		else:
			x = 4+x
			x = x+x
			m3 = x-m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		o0 = m3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))