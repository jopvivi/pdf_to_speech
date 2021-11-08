for f in *.pdf; do
  pdftotext "$f"
  echo -ne 'Please wait...\r'
  sleep 1
  echo -ne 'Please wait......          (33%)\r'
  sleep 1
  echo -ne 'Please wait.........       (66%)\r'
  sleep 1
  echo -ne 'Please wait............   (100%)\r'
  echo -ne 'Conversion complete!            \r'
  sleep 1
  echo -ne '\n'
done
