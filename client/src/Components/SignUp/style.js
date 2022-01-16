import { makeStyles } from "@mui/styles";

const useStyles = makeStyles({
  box: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    minHeight: "100vh",
    minWidth: "100vw",
    backgroundColor: "#EF4B4B",
    paddingLeft: 12,
    paddingRight: 12,
  },
  container: {
    backgroundColor: "#ffffff",
    boxShadow: "rgba(0, 0, 0, 0.35) 0px 5px 15px;",
    borderRadius: "8px",
    paddingTop: "24px",
    paddingBottom: "24px",
  },
});
export default useStyles;
