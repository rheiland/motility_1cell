#for i in $(seq 0 99); do
for i in $(seq 0 99); do
  echo "----------- run: $i"
  multirun p_motion_multirun.xml $i
  cat pc_combined_tracks.csv >> save.csv
done

